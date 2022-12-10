'''
Shortest Path 실전 문제 2. 미래 도시

방문 판매원 검성이는 X번 회사에 방문해 물건을 판매하고자 한다.
X번 회사로 가기 전에, 애기랑 K번 회사에서 소개팅을 하려고 한다.
검성이는 1번 회사에서 출발한다. K번 회사에서 소개팅을 하고, X번 회사로 물건을
판매하기 위한 최소 시간을 계산하세요.

도시 간 이동 시간은 1이고, 연결된 도시는 양방향으로 연결되어 있다.

Ex)
input
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

output
3
'''
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF]*(n+1) for i in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for z in range(1,n+1):
    for a in range(1,n + 1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][z]+graph[z][b])

if graph[k][x] == INF or graph[1][k] == INF:
    print(-1)
else:
    print(graph[1][k]+graph[k][x])