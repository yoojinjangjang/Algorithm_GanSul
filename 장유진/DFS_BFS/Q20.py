'''
감시 피하기
'''

import sys
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
hall = []
for i in range(n):
    hall.append(list(input().split()))

x_loc = []
t_loc = []
for i in range(n):
    for j in range(n):
        if hall[i][j] == 'X':
            x_loc.append((i,j))
        elif hall[i][j] == 'T':
            t_loc.append([i,j])

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def check_udlr(hall,loc,move):
    #hall 의 loc위치에서 move로 갔을 때 학생을 만나는지 검사
    nx = loc[0] + move[0]
    ny = loc[1] + move[1]
   # print(nx,ny)
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        return True
    elif hall[nx][ny] == 'O':
        return True
    elif hall[nx][ny] == 'S':
        return False
    else:
        loc[0] += move[0]
        loc[1] += move[1]
        if check_udlr(hall,loc,move):
            return True
        else:
            return False


def check_hall(hall,t_loc):
    for i in t_loc:
       # print("loc: ", i)
        for j in range(4):
            move = [dx[j],dy[j]]
         #   print("move: ", move)
            loc = deepcopy(i)
            if check_udlr(hall,loc,move):
                continue
            else:
                return False
    return True

checkFlag = False
for co in combinations(x_loc,3):
   # print("co: ",co)
    for loc in co:
        hall[loc[0]][loc[1]] = 'O'
   # print(hall)
    # 체크 함수
    t_temp = deepcopy(t_loc)
    if check_hall(hall,t_temp):
        checkFlag = True
        break
   # print("IM False")
   # print()
    for loc in co:
        hall[loc[0]][loc[1]] = 'X'


if checkFlag:
    print("YES")
else:
    print("NO")
