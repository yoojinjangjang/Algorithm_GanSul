'''
상하좌우 : N*N 크기의 정사각형 공간위의 여행자 A ( 가장 왼쪽 (1,1) 오른쪽아래 ( N,N )  )
         상하좌우 방향으로 이동 가능
         하나의 줄에 띄어쓰기 L(왼쪽),R(오른쪽),U(위),D(아래)
         계획서가 주어졌을 때 여행가 A의 최종적 도착 지점 좌표 출력

입력 : 공간의 크기 N
      계획서 내용

출력 : 여행자 A가 최종 도착할 지점의 좌표
'''
import sys
input = sys.stdin.readline

n = int(input())
data = list(input().split())

pos = [1,1]
for i in data:
    if i == 'R' and pos[1] != n:
        pos[1] += 1
    elif i == 'L' and pos[1] != 1:
        pos[1] -= 1
    elif i == 'U' and pos[0] != 1:
        pos[0] -= 1
    elif i == 'D' and pos[0] != n:
        pos[0] += 1
print(pos[0],pos[1])