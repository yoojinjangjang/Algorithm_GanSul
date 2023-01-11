'''
bfs 백준 4179. 불!

혜영이는 미로에서 일을 한다. 혜영이의 위치와 불의 위치를 감안해서
혜영이가 불에 타기 전에 미로에서 탈출할 수 있는 지의 여부, 그리고 얼마나 빨리 탈출할 수 있는 지를 결정해야한다.
미로의 가장자리에 접한 공간에서만 탈출할 수 있다.
혜영이와 불은 벽을 통과하지는 못한다.

입력
# : 벽
.: 지나갈 수 있는 공간
J : 혜영이의 미로에서 초기 위치(지나갈 수 있는 공간)
F : 불이 난 공간
4 4
####
#JF#
#..#
#..#

출력
혜영이가 불이 도달하기 전에 미로를 탈출할 수 없는 경우 IMPOSSIBLE을 출력한다.
혜영이가 미로에서 탈출할 수 있는 가장 빠른 시간을 출력한다.
3
'''
from collections import deque
r, c = map(int, input().split())  # 행, 열 입력
maze = [] # 사용자로부터 입력받는 미로 공간
for i in range(r):
    maze.append(list(input()))

j_queue = deque() #시작 지점 큐
f_queue = deque() #불난 지점 큐

fire_state = [[True] * c for _ in range(r)]
j_state = [[-1]*c for _ in range(r)]

for i in maze:
    print(i)

#시작점과 불난 지점 찾기 및 방문 그래프 초기화
for i in range(r):
    for j in range(c):
        if maze[i][j] == "J":  #J가 출발하는 곳의 화재 상태와 J상태 초기값 세팅
            j_queue.append((i, j))
            j_state[i][j] = 0
        elif maze[i][j] == "F":
            f_queue.append((i, j))
            fire_state[i][j] = False

print("초기 fire state @@@@@@@@@@@@@@@@@@@@@@@@@")
for i in fire_state:
    print(i)

print("초기 j_state @@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in j_state:
    print(i)

# 이동 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 혜영이의 움직이는 좌표를 큐에 넣는데, 더이상 움직일 곳이 없으면 반복을 종료한다.
def bfs():

    while j_queue:

        for _ in range(len(f_queue)):  #불이 발생한 곳들에 대한 bfs를 수행한다.
            x, y = f_queue.popleft()

            for i in range(4): # 불이 4방향으로 퍼지기 때문에 각 경우를 모두 처리한다.
                fx = x + dx[i]
                fy = y + dy[i]

                if fx < 0 or fx >= r or fy < 0 or fy >= c: # 이동한 불의 좌표가 그래프를 벗어났으면 다음 방향으로 넘어간다.
                    continue
                if maze[fx][fy] != "#" and fire_state[fx][fy]:
                    fire_state[fx][fy] = False
                    f_queue.append((fx, fy))

        for _ in range(len(j_queue)): #혜영이가 있는 곳들에 대한 bfs를 수행한다.
            x, y = j_queue.popleft()
            print("x = {}, y = {}".format(x,y))

            for i in range(4):
                jx = x + dx[i]
                jy = y + dy[i]

                if jx >= 0 and jx < r and jy >= 0 and jy < c:
                    if fire_state[jx][jy] and j_state[jx][jy] == -1 and maze[jx][jy] == ".": #해당 위치까지 거리보다 더 짧거나, 이동할 수 있는 곳이라면 최단거리를 갱신해준다.
                        j_state[jx][jy] = j_state[x][y] + 1
                        j_queue.append((jx, jy))
                if jx < 0 or jx >= r or jy < 0 or jy >= c:
                    print(jx)
                    print(jy)
                    return j_state[x][y]+1

        print("fire_state @@@@@@@@@@@@@@@@@@@@@@")
        for i in fire_state:
            print(i)
        print("j_state @@@@@@@@@@@@@@@@@@@@@@@@@")

        for i in j_state:
            print(i)


    return "IMPOSSIBLE"

print(bfs())




