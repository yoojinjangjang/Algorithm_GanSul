'''
DFS/BFS 기출 문제 15. 특정 거리의 도시 찾기
1~N번까지의 도시와 M개의 단방향 도로가 존재한다. 특정한 도시 x로부터 출발하여 도달할 수 있는 모든
도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.

답안 참고하였음.

n = 도시의 수
m = 도로 개수
k = 최단 거리
x = 출발 도시
'''
import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n+1):
    graph.append([])

#각 도시가 갖고 있는 단방향 도로 배열
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#각 도시의 방문 여부 및 최단 거리를 나타내는 리스트
cities = [-1]*(n+1)
cities[x] = 0 #시작 도시는 방문 처리

queue = deque([x])

while queue:

    start = queue.popleft()

    for next_city in graph[start]:

        #아직 방문하지 않은 도시라면 이전 도시에서 현재 도시로 이동하였으므로 이전 최단거리를 더해준다.
        # 이동하였으므로 +1 을 해준다.
        # cities[next_city] == -1 이라는 것은 해당 도시를 처음 방문한 것이므로, 이때가 최단 거리가 되므로
        # cities[next_city] == -1 일 때만 고려하면 된다.
        if cities[next_city] == -1:
            cities[next_city] = cities[start] + 1
            queue.append(next_city)

check = False
print(cities)
for i in range(1, n+1):
    if cities[i] == k:
        check = True
        print(i)

if not check:
    print("-1")

