'''
구현 실전 문제 4. 게임 개발
1 x 1 크기의 칸으로 이루어진 N x M 의 게임 맵 안에서 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.


'''

import sys
n, m = map(int, sys.stdin.readline().split())
col, low, dir = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cnt = 1
gm = []
while len(gm) < n:
    gm.append(list(map(int, sys.stdin.readline().split())))

while True:
    dir = (dir+1)%4
    temp_c = col +dx[dir]
    temp_l = low +dy[dir]

    if gm[temp_c][temp_l] == 1:
        temp_c = col-dx[dir]
        temp_l = low-dy[dir]

        col = temp_c
        low = temp_l

        if gm[col][low] == 1:
            break

        else:
            gm[col][low] = 1
            cnt += 1
        continue
    cnt += 1
    col = temp_c
    low = temp_l
    gm[col][low] = 1
print(cnt)

