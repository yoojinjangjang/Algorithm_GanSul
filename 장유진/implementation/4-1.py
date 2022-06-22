'''
Q4-1] 상하좌우
: 여행가 A는 N*N 크기의 정사각형 공간, 왼쪽위 -시작 좌표(1,1), 오른쪽 아래 (N,N)
: 계획표 L(왼쪽),R(오른쪽),U(위쪽),D(아래쪽) , 최종적 도착 지점 좌표 출력

입력 : 공간의 크기 N
      여행계획서
출력 : 최종적으로 도착할 지점의 좌표
'''

import sys
input = sys.stdin.readline

n = int(input())
plan = list(input().split())
location = [1,1]
for p in plan:
    if p == 'L' and location[1] != 1:
        location[1] -= 1
    elif p == 'R' and location[1] != n:
        location[1] += 1
    elif p == 'U' and location[0] != 1:
        location[0] -= 1
    elif p == 'D' and location[0] != n:
        location[0] += 1
print(location[0],location[1])