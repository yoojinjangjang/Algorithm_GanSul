'''
DFS/BFS 기출 문제 16. 연구소
연구소는 N x M 크기의 직사각형으로 나타낼 수 있으며, 직사각형은 1 x 1 크기의
정사각형으로 나누어져 있습니다.
연구소는 빈칸, 벽으로 이루어져 있으며, 일부 칸에는 바이러스가 존재합니다. 이 바이러스는 상하좌우로
인접한 빈칸으로 모두 퍼져나갈 수 있습니다. 새로 세울 수 있는 벽의 개수는 3개이며,
꼭 3개를 세워야합니다.
벽 3개를 적절한 위치에 세워서 바이러스가 퍼질 수 없는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하세요.
1 = 벽
2 = 바이러스
Ex)
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
#dfs 로 해결

n, m = map(int, input().split())
lab = []
temp = [[0]*m for _ in range(n)]
result = 0
for _ in range(n):
    lab.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)
def count_0():

    zero_check = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero_check += 1

    return zero_check


def dfs(wall):
    global result
    if wall == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(count_0(), result)
        return

    else:
        for i in range(n):
            for j in range(m):
                if lab[i][j] == 0:
                    lab[i][j] = 1
                    wall += 1
                    dfs(wall)
                    lab[i][j] = 0
                    wall -= 1

dfs(0)
print(result)