'''
Shortest_Path 실전 문제 3. 전보

X도시에서 최대한 많은 도시로 메시지를 보내자고 한다. 메시지는 도시 C에서 출발하여
각 도시의 통로를 거쳐, 최대한 많이 퍼져나간다.
도시 C에서 보낸 메시지를 받게 되는 도시의 수와 메시지를 받는 데까지 걸리는 시간을 구하시오.

Ex)
input
3 2 1
1 2 4
1 3 2

output
2 4
'''
import sys
import heapq
input = sys.stdin.readline
n, m, start = map(int, input().split())
INF = int(1e9)
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


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


dijkstra(start)
count = 0
max_d = 0
for i in distance:
    if i != INF:
        count += 1
        max_d = max(max_d, i)

print(count -1, max_d)
