'''
음료수 얼려 먹기
입력: N,M
     얼음 틀의 형태(0:구멍뚫림,1:그렇지않음)
출력: 만들 수 있는 아이스크림 개수
'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
ice = []
for i in range(n):
    ice.append(list(map(int,input().strip())))

def bfs(graph, start, visited): # bfs 쓸거임
    queue = deque()
    visited[start] = True
    queue.append(start)
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

loc = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우 검사 용임
graph = [[] for _ in range(n*m)]
visited = [True] * (n*m)

for i in range(n): #행
    for j in range(m): #열
        # 행과 열을 돌면서 각 노드가 0일 경우 인접 노드를 찾아서  graph 에 넣어주려고 함!
        if ice[i][j] == 0:
            visited[i*m+j] = False
            for l in loc:
                if 0<= i+l[0] < n and 0 <= j+l[1] < m and ice[i+l[0]][j+l[1]] == 0:
                    graph[i*m+j].append((i+l[0])*m+j+l[1])

answer = 0
for v in range(n*m):
    if visited[v] == False:
        bfs(graph,v,visited)
        answer += 1


print(answer)