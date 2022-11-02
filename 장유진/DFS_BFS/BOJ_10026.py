'''
적록색약
빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 NXN인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져
있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의
차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다.)

입력: 첫째 줄- N
둘째 줄 - N개: 그림

출력: 적록색약이 아닌 사람 구역 개수 적록색약 구역 수
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
space = []

for _ in range(n):
    space.append(list(input().strip()))

color = {"R": ["R", "G"], "G": ["R", "G"], "B": ["B"]}
color_normal = {"R": ["R"], "G": ["G"], "B": ["B"]}


def get_num(color_yn):
    visited = [[False] * n for _ in range(n)]  # 중첩 list 생성시 잘못된 방법으로 생성하면 서로가 서로를 공유함 ! 안돼
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    space_num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            space_num += 1
            visited[i][j] = True
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for l in range(4):
                    nx = x + dx[l]
                    ny = y + dy[l]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue
                    if visited[nx][ny] is False and space[nx][ny] in color_yn[space[x][y]]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
    return space_num


print(get_num(color_normal))
print(get_num(color))
